using UnityEngine;
using System.Collections.Generic;
using System.Collections;

class CarController : MonoBehaviour
{
	[SerializeField] SteeringUIManager steeringManager;
	[SerializeField] string deviceName = "raspberrypi";

	CommunicationMedium communication;

	private void Start ()
	{
		this.communication = new BluetoothCommunicationManager( this.deviceName );
		//this.communication = new MockCommunicationManager();

		this.KeepConnectingUntilSuccessfull();
	}

	private void Update ()
	{
		if ( !this.communication.isConnected )
			return;

		this.SendSteer( this.steeringManager.GetMovementDirection().x );
		this.SendDrive( this.steeringManager.GetMovementDirection().y );
	}

	void KeepConnectingUntilSuccessfull() 
	{
		this.communication.onConnected += this.StopTryingToConnect;
		this.communication.onConnectionFailed += this.TryReconnect;

		this.communication.Connect();
	}

	void StopTryingToConnect() {
		this.communication.onConnectionFailed -= this.TryReconnect;
	}

	void TryReconnect() {
		this.communication.Connect();
	}

	void SendDrive ( float value )
	{
		byte driveValue = ConversionHelper.FloatToInt8( value );

		this.SendCommand( ECommandCodes.Drive, new byte[] { driveValue } );
	}

	void SendSteer ( float value )
	{
		byte steerValue = ConversionHelper.FloatToInt8( value );

		this.SendCommand( ECommandCodes.Steer, new byte[] { steerValue } );
	}


	void SendCommand ( ECommandCodes command, byte[] data )
	{
		List<byte> sendData = new List<byte>( data );

		sendData.Insert( 0, (byte)command );

		//Debug.Log( "Sending data: " + string.Join( ", ", sendData.ToArray() ) );

		this.communication.SendData( sendData.ToArray() );
	}
}
