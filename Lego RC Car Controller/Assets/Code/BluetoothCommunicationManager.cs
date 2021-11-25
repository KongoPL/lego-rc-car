using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using ArduinoBluetoothAPI;

public class BluetoothCommunicationManager : CommunicationMedium 
{
	BluetoothHelper bluetoothHelper;
	string deviceName;

	public BluetoothCommunicationManager ( string deviceName )
	{
		BluetoothHelper.BLE = false;

		this.bluetoothHelper = BluetoothHelper.GetInstance();
		this.deviceName = deviceName;
	}

	override public void Connect()
	{
		this.bluetoothHelper.OnConnected += this.OnConnectedInternal;
		this.bluetoothHelper.OnConnectionFailed += this.OnConnectionFailedInternal;
		this.bluetoothHelper.OnDataReceived += this.OnDataReceivedInternal;
		this.bluetoothHelper.setFixedLengthBasedStream( 1 ); //data is received byte by byte
		this.bluetoothHelper.setDeviceName( this.deviceName );
		this.bluetoothHelper.Connect();
	}

	void OnConnectedInternal ( BluetoothHelper helper )
	{
		helper.StartListening();

		
		this.OnConnected();
	}

	void OnConnectionFailedInternal ( BluetoothHelper helper )
	{
		Debug.LogError( "Failed to connect" );
		this.OnConnectionFailed();
	}


	void OnDataReceivedInternal ( BluetoothHelper helper )
	{
		//string msg = helper.Read();
	}

	public void Disconnect ()
	{
		bluetoothHelper.Disconnect();

		this.OnDisconnected();
	}


	override public void SendData ( byte[] data )
	{
		this.bluetoothHelper.SendData( data );
	}
}
