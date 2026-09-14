# Settlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**merchant_uuid** | **UUID** |  | 
**period_from** | **datetime** |  | 
**period_to** | **datetime** |  | 
**idempotency_key** | **str** |  | 
**merchant_payable_amount** | **int** |  | 
**settled_amount** | **int** |  | 
**currency** | **str** |  | 
**status** | **str** |  | 
**stripe_transfer_id** | **str** |  | 
**notes** | **str** |  | 
**settled_at** | **datetime** |  | 
**expires_at** | **datetime** |  | 
**reviewed_by_user_uuid** | **UUID** |  | 
**reviewed_at** | **datetime** |  | 
**rejection_reason** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from maytes_api_client.models.settlement import Settlement

# TODO update the JSON string below
json = "{}"
# create an instance of Settlement from a JSON string
settlement_instance = Settlement.from_json(json)
# print the JSON string representation of the object
print(Settlement.to_json())

# convert the object into a dict
settlement_dict = settlement_instance.to_dict()
# create an instance of Settlement from a dict
settlement_from_dict = Settlement.from_dict(settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


