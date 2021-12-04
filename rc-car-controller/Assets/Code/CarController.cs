using UnityEngine;
using System.Collections.Generic;
using System.Collections;

class CarController : MonoBehaviour
{
	[SerializeField] SteeringUIManager steeringManager;
	[SerializeField] string deviceName = "raspberrypi";

	CommunicationMedium communication;
	bool failedLastConnection = true;
	bool isHandbrakeEnabled = false;

	void Start ()
	{
		this.communication = new BluetoothCommunicationManager( this.deviceName );
		//this.communication = new MockCommunicationManager( true );

		this.InitConnectingUntilSuccessfull();
	}

	void Update ()
	{
		if ( !this.communication.isConnected )
			return;

		this.SendSteer( this.steeringManager.GetMovementDirection().x );
		this.SendDrive( this.steeringManager.GetMovementDirection().y );

		bool isNowHandbrakeEnabled = this.steeringManager.handbrakeEnabled;

		if ( isNowHandbrakeEnabled )
		{
			this.SendHandbrakeStart();

			this.isHandbrakeEnabled = true;
		}
		else if ( this.isHandbrakeEnabled )
		{
			this.SendHandbrakeEnd();

			this.isHandbrakeEnabled = false;
		}
	}

	void InitConnectingUntilSuccessfull()
	{
		this.StartCoroutine( this.KeepConnectingUntilSuccessfull() );
	}

	IEnumerator KeepConnectingUntilSuccessfull() 
	{
		this.communication.onConnectionFailed -= this.InitConnectingUntilSuccessfull; // Stop reconnecting when connection failed
		this.communication.onConnectionFailed += this.MarkConnectionAsFailed;
		this.communication.onConnected += this.OnKeepConnectionSuccessfull;

		this.failedLastConnection = true;
		int connectAttempt = 0;

		while ( !this.communication.isConnected )
		{
			if ( this.failedLastConnection )
			{
				connectAttempt++;

				this.failedLastConnection = false;
				this.steeringManager.SetStatusConnecting( connectAttempt );
				this.communication.Connect();

				yield return new WaitForSeconds( 5.0f );
			}
			else
			{
				yield return new WaitForSeconds( 0.2f );

				continue;
			}
		}

		yield break;
	}

	void MarkConnectionAsFailed ()
	{
		this.failedLastConnection = true;
	}

	void OnKeepConnectionSuccessfull ()
	{
		this.communication.onConnectionFailed -= this.MarkConnectionAsFailed;
		this.communication.onConnectionFailed += this.InitConnectingUntilSuccessfull; // When connection resets, it will reconnect again
		this.steeringManager.SetStatusConnected();
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


	void SendHandbrakeStart()
	{
		this.SendCommand( ECommandCodes.HandbrakeStart );
	}


	void SendHandbrakeEnd()
	{
		this.SendCommand( ECommandCodes.HandbrakeEnd );
	}


	void SendCommand ( ECommandCodes command )
	{
		this.SendCommand( command, new byte[0] );
	}

	void SendCommand ( ECommandCodes command, byte[] data )
	{
		List<byte> sendData = new List<byte>( data );

		sendData.Insert( 0, (byte)command );

		//Debug.Log( "Sending data: " + string.Join( ", ", sendData.ToArray() ) );

		this.communication.SendData( sendData.ToArray() );
	}
}
