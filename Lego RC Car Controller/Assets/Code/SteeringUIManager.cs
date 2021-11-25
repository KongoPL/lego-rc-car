using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SteeringUIManager : MonoBehaviour
{
	[SerializeField] FixedJoystick steeringJoystick;
	[SerializeField] FixedJoystick driveJoystick;
	[SerializeField] Text statusText;

	public Vector2 GetMovementDirection()
	{
		return new Vector2(
			this.steeringJoystick.Direction.x,
			this.driveJoystick.Direction.y
		);
	}


	public void SetStatusConnecting ( int attempt = 0 )
	{

	}


	public void SetStatusConnected()
	{

	}
}
