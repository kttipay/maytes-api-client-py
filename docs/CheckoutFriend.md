# CheckoutFriend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**mobile** | **str** | E.164, e.g. +61412345678 | 
**email** | **str** |  | [optional] 
**amount** | **int** | This friend’s share in minor units. Give it for every friend or for none. | [optional] 
**items** | [**List[CheckoutFriendItem]**](CheckoutFriendItem.md) | The cart lines this friend pays for (item_assignment only). Give it for every friend or for none. | [optional] 

## Example

```python
from maytes_api_client.models.checkout_friend import CheckoutFriend

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutFriend from a JSON string
checkout_friend_instance = CheckoutFriend.from_json(json)
# print the JSON string representation of the object
print(CheckoutFriend.to_json())

# convert the object into a dict
checkout_friend_dict = checkout_friend_instance.to_dict()
# create an instance of CheckoutFriend from a dict
checkout_friend_from_dict = CheckoutFriend.from_dict(checkout_friend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


