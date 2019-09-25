using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading;

namespace CoinAPI.WebSocket.V1
{
    public class QueueThread<T> : IDisposable
    {
        private readonly ManualResetEvent _messagesBufferEvent = new ManualResetEvent(false);
        private readonly TimeSpan _messagesRouterTimeout = TimeSpan.FromSeconds(1);
        private readonly int? _bufferCapacity;
        private Thread _messagesRouterThread;
        private readonly Queue<T> _messagesBuffer = new Queue<T>();

        public delegate void ItemDequeuedEventHandler(object sender, T item);
        public event ItemDequeuedEventHandler ItemDequeuedEvent;

        private readonly CancellationTokenSource _cts = new CancellationTokenSource();

        public QueueThread(int? bufferCapacity = null)
        {
            _bufferCapacity = bufferCapacity;
            _messagesRouterThread = new Thread(MessagesRouter_Thread)
            {
                IsBackground = true,
                Name = GetType().FullName,
                Priority = ThreadPriority.Highest
            };
            _messagesRouterThread.Start();
        }

        public void Dispose()
        {
            _cts.Cancel();
            _cts.Dispose();
        }

        private void MessagesRouter_Thread()
        {
            while (!_cts.IsCancellationRequested)
            {
                try
                {
                    while (_messagesBufferEvent.WaitOne(_messagesRouterTimeout))
                    {
                        T item;
                        lock (_messagesBuffer)
                        {
                            if (_messagesBuffer.Count == 0)
                            {
                                break;
                            }

                            item = _messagesBuffer.Dequeue();
                        }

                        ItemDequeuedEvent?.Invoke(this, item);
                    }

                    _messagesBufferEvent.Reset();
                }
                catch (Exception ex)
                {
                    Debug.WriteLine(ex.ToString());
                }
            }
        }

        public bool Enqueue(T item)
        {
            lock (_messagesBuffer)
            {
                if (_bufferCapacity.HasValue && _messagesBuffer.Count >= _bufferCapacity.Value)
                {
                    return false;
                }

                _messagesBuffer.Enqueue(item);
            }

            _messagesBufferEvent.Set();
            return true;
        }

        public int QueueSize
        {
            get
            {
                lock (_messagesBuffer)
                {
                    return _messagesBuffer.Count;
                }
            }
        }
    }
}
