using System;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.IO;
using Utf8Json;

namespace CoinAPI.WebSocket.V1
{
    internal static class WSUtils
    {
        private static readonly int ReceiveBufferSize = 8192;

        internal async static Task<MessageData> ReceiveMessage(
            System.Net.WebSockets.WebSocket webSocket, long maxSize = long.MaxValue)
        {
            ArraySegment<Byte> buffer = new ArraySegment<byte>(new Byte[ReceiveBufferSize]);
            WebSocketReceiveResult result = null;

            using (var ms = new MemoryStream())
            {
                do
                {
                    result = await webSocket.ReceiveAsync(buffer, CancellationToken.None);
                    ms.Write(buffer.Array, buffer.Offset, result.Count);
                    if (ms.Length > maxSize)
                    {
                        throw new InvalidOperationException("Maximum size of the message was exceeded.");
                    }
                }
                while (!result.EndOfMessage);

                ms.Seek(0, SeekOrigin.Begin);

                return new MessageData
                {
                    Data = ms.ToArray(),
                    MessageType = result.MessageType
                };
            }
        }

        public static T ParseMessage<T>(MessageData messageData)
        {
            var jsonString = Encoding.ASCII.GetString(messageData.Data);
            var messageObject = JsonSerializer.Deserialize<T>(jsonString);

            return messageObject;
        }

        public static async Task SendMessage(ArraySegment<byte> data,
            System.Net.WebSockets.WebSocket webSocket)
        {
            await webSocket.SendAsync(data, WebSocketMessageType.Text,
                endOfMessage: true,
                cancellationToken: CancellationToken.None);
        }
    }
}
