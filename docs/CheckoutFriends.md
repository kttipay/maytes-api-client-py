# CheckoutFriends


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | How many friends will split, not counting the customer. Give this or &#x60;people&#x60;. | [optional] 
**people** | [**List[CheckoutFriend]**](CheckoutFriend.md) | The friends, optionally with their shares. Give this or &#x60;count&#x60;. | [optional] 

## Example

```python
from maytes_api_client.models.checkout_friends import CheckoutFriends

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutFriends from a JSON string
checkout_friends_instance = CheckoutFriends.from_json(json)
# print the JSON string representation of the object
print(CheckoutFriends.to_json())

# convert the object into a dict
checkout_friends_dict = checkout_friends_instance.to_dict()
# create an instance of CheckoutFriends from a dict
checkout_friends_from_dict = CheckoutFriends.from_dict(checkout_friends_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


