using UnityEngine;
using UnityEngine.Events;
using UnityEngine.EventSystems;
using UnityEngine.UI;

public class ButtonPressDecetion : MonoBehaviour, IPointerDownHandler, IPointerUpHandler
{
	public UnityEvent onClickDown;
	public UnityEvent onClickUp;

	public void OnPointerDown ( PointerEventData eventData )
	{
		onClickDown?.Invoke();
	}

	public void OnPointerUp ( PointerEventData eventData )
	{
		onClickUp?.Invoke();
	}
}