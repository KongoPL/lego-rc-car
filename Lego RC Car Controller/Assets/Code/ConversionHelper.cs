using UnityEngine;
class ConversionHelper
{
	public static byte FloatToInt8(float value) 
	{
		return (byte)Mathf.RoundToInt( value * ( Mathf.Sign( value ) == 1 ? 127 : 128 ) );
	}
}