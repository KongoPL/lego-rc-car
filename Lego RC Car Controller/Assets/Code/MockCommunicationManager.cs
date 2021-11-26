using UnityEngine;
using System.Collections.Generic;

class MockCommunicationManager : CommunicationMedium
{
	public bool connectionWorks;

	public MockCommunicationManager ( bool connectionWorks = true )
	{
		this.connectionWorks = connectionWorks;
	}

	override public void Connect ()
	{
		if ( this.connectionWorks )
		{
			Debug.Log( "Connected to device!" );

			this.OnConnected();
		}
		else
		{
			Debug.LogError( "Failed connecting to the device!" );

			this.OnConnectionFailed();
		}
	}

	override public void SendData ( byte[] data )
	{
		Debug.Log( "Sending data: " + string.Join(", ", data) );
	}
}