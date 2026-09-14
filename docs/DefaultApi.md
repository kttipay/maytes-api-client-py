# maytes_api_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_checkout**](DefaultApi.md#cancel_checkout) | **POST** /api/merchant/v1/checkouts/{checkoutUuid}/cancel | Cancel authorized checkout
[**capture_checkout**](DefaultApi.md#capture_checkout) | **POST** /api/merchant/v1/checkouts/{checkoutUuid}/capture | Capture authorized checkout
[**create_checkout**](DefaultApi.md#create_checkout) | **POST** /api/merchant/v1/checkouts | Create a new checkout
[**get_checkout**](DefaultApi.md#get_checkout) | **GET** /api/merchant/v1/checkouts/{checkoutUuid} | Get checkout details
[**get_health**](DefaultApi.md#get_health) | **GET** /api/health | Health check
[**get_o_auth_token**](DefaultApi.md#get_o_auth_token) | **POST** /oauth/token | Issue an access token
[**get_settlement**](DefaultApi.md#get_settlement) | **GET** /api/merchant/v1/settlements/{uuid} | Get a settlement by UUID
[**list_settlements**](DefaultApi.md#list_settlements) | **GET** /api/merchant/v1/settlements | List settlements for this merchant
[**refund_checkout**](DefaultApi.md#refund_checkout) | **POST** /api/merchant/v1/checkouts/{checkoutUuid}/refund | Refund a captured checkout


# **cancel_checkout**
> CancelCheckoutResponse cancel_checkout(checkout_uuid, cancel_checkout_request)

Cancel authorized checkout

### Example

* Bearer (JWT) Authentication (bearer):

```python
import maytes_api_client
from maytes_api_client.models.cancel_checkout_request import CancelCheckoutRequest
from maytes_api_client.models.cancel_checkout_response import CancelCheckoutResponse
from maytes_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = maytes_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = maytes_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with maytes_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = maytes_api_client.DefaultApi(api_client)
    checkout_uuid = 'checkout_uuid_example' # str | 
    cancel_checkout_request = maytes_api_client.CancelCheckoutRequest() # CancelCheckoutRequest | 

    try:
        # Cancel authorized checkout
        api_response = api_instance.cancel_checkout(checkout_uuid, cancel_checkout_request)
        print("The response of DefaultApi->cancel_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_uuid** | **str**|  | 
 **cancel_checkout_request** | [**CancelCheckoutRequest**](CancelCheckoutRequest.md)|  | 

### Return type

[**CancelCheckoutResponse**](CancelCheckoutResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**422** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **capture_checkout**
> CaptureCheckoutResponse capture_checkout(checkout_uuid, capture_checkout_request)

Capture authorized checkout

### Example

* Bearer (JWT) Authentication (bearer):

```python
import maytes_api_client
from maytes_api_client.models.capture_checkout_request import CaptureCheckoutRequest
from maytes_api_client.models.capture_checkout_response import CaptureCheckoutResponse
from maytes_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = maytes_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = maytes_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with maytes_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = maytes_api_client.DefaultApi(api_client)
    checkout_uuid = 'checkout_uuid_example' # str | 
    capture_checkout_request = maytes_api_client.CaptureCheckoutRequest() # CaptureCheckoutRequest | 

    try:
        # Capture authorized checkout
        api_response = api_instance.capture_checkout(checkout_uuid, capture_checkout_request)
        print("The response of DefaultApi->capture_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->capture_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_uuid** | **str**|  | 
 **capture_checkout_request** | [**CaptureCheckoutRequest**](CaptureCheckoutRequest.md)|  | 

### Return type

[**CaptureCheckoutResponse**](CaptureCheckoutResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**422** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_checkout**
> CreateCheckoutResponse create_checkout(create_checkout_request)

Create a new checkout

### Example

* Bearer (JWT) Authentication (bearer):

```python
import maytes_api_client
from maytes_api_client.models.create_checkout_request import CreateCheckoutRequest
from maytes_api_client.models.create_checkout_response import CreateCheckoutResponse
from maytes_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = maytes_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = maytes_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with maytes_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = maytes_api_client.DefaultApi(api_client)
    create_checkout_request = maytes_api_client.CreateCheckoutRequest() # CreateCheckoutRequest | 

    try:
        # Create a new checkout
        api_response = api_instance.create_checkout(create_checkout_request)
        print("The response of DefaultApi->create_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_checkout_request** | [**CreateCheckoutRequest**](CreateCheckoutRequest.md)|  | 

### Return type

[**CreateCheckoutResponse**](CreateCheckoutResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**409** |  |  -  |
**422** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkout**
> GetCheckoutResponse get_checkout(checkout_uuid, merchant_order_id=merchant_order_id)

Get checkout details

### Example

* Bearer (JWT) Authentication (bearer):

```python
import maytes_api_client
from maytes_api_client.models.get_checkout_response import GetCheckoutResponse
from maytes_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = maytes_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = maytes_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with maytes_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = maytes_api_client.DefaultApi(api_client)
    checkout_uuid = 'checkout_uuid_example' # str | 
    merchant_order_id = 'merchant_order_id_example' # str |  (optional)

    try:
        # Get checkout details
        api_response = api_instance.get_checkout(checkout_uuid, merchant_order_id=merchant_order_id)
        print("The response of DefaultApi->get_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_uuid** | **str**|  | 
 **merchant_order_id** | **str**|  | [optional] 

### Return type

[**GetCheckoutResponse**](GetCheckoutResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**422** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health**
> HealthResponse get_health()

Health check

### Example


```python
import maytes_api_client
from maytes_api_client.models.health_response import HealthResponse
from maytes_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = maytes_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with maytes_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = maytes_api_client.DefaultApi(api_client)

    try:
        # Health check
        api_response = api_instance.get_health()
        print("The response of DefaultApi->get_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_token**
> OAuthTokenResponse get_o_auth_token(o_auth_token_request)

Issue an access token

### Example


```python
import maytes_api_client
from maytes_api_client.models.o_auth_token_request import OAuthTokenRequest
from maytes_api_client.models.o_auth_token_response import OAuthTokenResponse
from maytes_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = maytes_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with maytes_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = maytes_api_client.DefaultApi(api_client)
    o_auth_token_request = maytes_api_client.OAuthTokenRequest() # OAuthTokenRequest | 

    try:
        # Issue an access token
        api_response = api_instance.get_o_auth_token(o_auth_token_request)
        print("The response of DefaultApi->get_o_auth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_o_auth_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_token_request** | [**OAuthTokenRequest**](OAuthTokenRequest.md)|  | 

### Return type

[**OAuthTokenResponse**](OAuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid grant or request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settlement**
> GetSettlementResponse get_settlement(uuid)

Get a settlement by UUID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import maytes_api_client
from maytes_api_client.models.get_settlement_response import GetSettlementResponse
from maytes_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = maytes_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = maytes_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with maytes_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = maytes_api_client.DefaultApi(api_client)
    uuid = 'uuid_example' # str | Settlement UUID

    try:
        # Get a settlement by UUID
        api_response = api_instance.get_settlement(uuid)
        print("The response of DefaultApi->get_settlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_settlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Settlement UUID | 

### Return type

[**GetSettlementResponse**](GetSettlementResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_settlements**
> ListSettlementsResponse list_settlements(offset=offset, limit=limit, sort_dir=sort_dir, sort_by=sort_by, created_before=created_before, created_after=created_after, status=status)

List settlements for this merchant

Returns settlements for the authenticated merchant. Default sort: created_at ASC.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import maytes_api_client
from maytes_api_client.models.list_settlements_response import ListSettlementsResponse
from maytes_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = maytes_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = maytes_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with maytes_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = maytes_api_client.DefaultApi(api_client)
    offset = None # object | Pagination offset (default 0) (optional)
    limit = None # object | Max records to return (default 50, max 200) (optional)
    sort_dir = 'sort_dir_example' # str | Sort direction (default: asc) (optional)
    sort_by = 'sort_by_example' # str | Field to sort by (default: created_at) (optional)
    created_before = None # object | Include settlements created at or before this ISO-8601 timestamp (optional)
    created_after = None # object | Include settlements created at or after this ISO-8601 timestamp (optional)
    status = 'status_example' # str | Filter by status (optional)

    try:
        # List settlements for this merchant
        api_response = api_instance.list_settlements(offset=offset, limit=limit, sort_dir=sort_dir, sort_by=sort_by, created_before=created_before, created_after=created_after, status=status)
        print("The response of DefaultApi->list_settlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_settlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | [**object**](.md)| Pagination offset (default 0) | [optional] 
 **limit** | [**object**](.md)| Max records to return (default 50, max 200) | [optional] 
 **sort_dir** | **str**| Sort direction (default: asc) | [optional] 
 **sort_by** | **str**| Field to sort by (default: created_at) | [optional] 
 **created_before** | [**object**](.md)| Include settlements created at or before this ISO-8601 timestamp | [optional] 
 **created_after** | [**object**](.md)| Include settlements created at or after this ISO-8601 timestamp | [optional] 
 **status** | **str**| Filter by status | [optional] 

### Return type

[**ListSettlementsResponse**](ListSettlementsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_checkout**
> refund_checkout(checkout_uuid, create_refund_request)

Refund a captured checkout

Initiates a full refund of the captured payment. Returns 204 immediately; Stripe confirms asynchronously via webhook. Poll GET /checkouts/:uuid for status and refund details.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import maytes_api_client
from maytes_api_client.models.create_refund_request import CreateRefundRequest
from maytes_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = maytes_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = maytes_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with maytes_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = maytes_api_client.DefaultApi(api_client)
    checkout_uuid = 'checkout_uuid_example' # str | 
    create_refund_request = maytes_api_client.CreateRefundRequest() # CreateRefundRequest | 

    try:
        # Refund a captured checkout
        api_instance.refund_checkout(checkout_uuid, create_refund_request)
    except Exception as e:
        print("Exception when calling DefaultApi->refund_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_uuid** | **str**|  | 
 **create_refund_request** | [**CreateRefundRequest**](CreateRefundRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**401** |  |  -  |
**402** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

