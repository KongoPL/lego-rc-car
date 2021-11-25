using UnityEngine;
using System.Collections.Generic;

class MockCommunicationManager : CommunicationMedium
{
	override public void Connect ()
	{
		Debug.Log( "Connected to device!" );

		this.OnConnected();
	}

	override public void SendData ( byte[] data )
	{
		Debug.Log( "Sending data: " + string.Join(", ", data) );
	}
}