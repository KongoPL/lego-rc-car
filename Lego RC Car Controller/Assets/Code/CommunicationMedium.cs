using UnityEngine;

abstract public class CommunicationMedium : MonoBehaviour
{
	public delegate void OnConnectedEvent ();
	public event OnConnectedEvent onConnected;

	public delegate void OnDisconnectedEvent ();
	public event OnDisconnectedEvent onDisconnected;

	public delegate void OnConnectionFailedEvent ();
	public event OnConnectionFailedEvent onConnectionFailed;

	public bool isConnected = false;

	abstract public void Connect ();
	abstract public void SendData ( byte[] data );

	protected void OnConnected ()
	{
		this.isConnected = true;

		this.onConnected?.Invoke();
	}

	protected void OnDisconnected ()
	{
		this.isConnected = false;

		this.onDisconnected?.Invoke();
	}

	protected void OnConnectionFailed ()
	{
		this.onConnectionFailed?.Invoke();
	}
}