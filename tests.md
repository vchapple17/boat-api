# boat-api Testing
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [boat-api Testing](#boat-api-testing)
	- [Pre-Clean](#pre-clean)
- [Boat: Read All](#boat-read-all)
	- [Test 1: Get all boats](#test-1-get-all-boats)
		- [Request](#request)
		- [Expected Response](#expected-response)
- [Boat: Create & Read Boat](#boat-create-read-boat)
	- [Test 2: Create a new boat](#test-2-create-a-new-boat)
		- [Request](#request)
		- [Expected Response](#expected-response)
	- [Test 3: URL from Test 2 Works](#test-3-url-from-test-2-works)
		- [Request](#request)
		- [Expected Response](#expected-response)
	- [Test 4: ID from Test 2 Works](#test-4-id-from-test-2-works)
		- [Request](#request)
		- [Expected Response](#expected-response)
	- [Test 5: Get All Boats After Test 2](#test-5-get-all-boats-after-test-2)
		- [Request](#request)
		- [Expected Response](#expected-response)
- [Boat: Edit Boat](#boat-edit-boat)
	- [Test 6: Edit Boat Name, Type, Length](#test-6-edit-boat-name-type-length)
		- [Request](#request)
		- [Expected Response](#expected-response)
	- [Test 7: Check Boat Updated Correctly](#test-7-check-boat-updated-correctly)
		- [Request](#request)
		- [Expected Response](#expected-response)
- [Slip: Read All Slips](#slip-read-all-slips)
	- [Test 8: Get all slips](#test-8-get-all-slips)
		- [Request](#request)
		- [Expected Response](#expected-response)
- [Slip: Create & Read Slip](#slip-create-read-slip)
	- [Test 9: Create a new slip](#test-9-create-a-new-slip)
		- [Request](#request)
		- [Expected Response](#expected-response)
	- [Test 10: URL from Test 8 Works](#test-10-url-from-test-8-works)
	- [Test 11: ID from Test 8 Works](#test-11-id-from-test-8-works)
	- [Test 12: Get All Slips After Test 8](#test-12-get-all-slips-after-test-8)
- [Slip: Edit Slip](#slip-edit-slip)
	- [Test 13: Edit Slip Number](#test-13-edit-slip-number)
	- [Test 14: Check Slip Number Updated Correctly](#test-14-check-slip-number-updated-correctly)
- [Boat Arrival Case 1](#boat-arrival-case-1)
	- [Test 15: Verify Slip is Empty](#test-15-verify-slip-is-empty)
	- [Test 16: Verify Boat is At Sea](#test-16-verify-boat-is-at-sea)
	- [Test 17: Boat Arrival](#test-17-boat-arrival)
	- [Test 18: Verify Boat is Not at Sea](#test-18-verify-boat-is-not-at-sea)
	- [Test 19: Verify Slip lists the Boat and URL](#test-19-verify-slip-lists-the-boat-and-url)
- [Boat Arrival Case 2](#boat-arrival-case-2)
	- [Test 20: Verify Slip is Occupied](#test-20-verify-slip-is-occupied)
	- [Test 21: Verify Boat is At Sea](#test-21-verify-boat-is-at-sea)
	- [Test 22: Boat Arrival Denied (403 - Slip Occupied)](#test-22-boat-arrival-denied-403-slip-occupied)
	- [Test 23: Verify Boat is Unchanged](#test-23-verify-boat-is-unchanged)
	- [Test 24: Verify Slip is Unchanged](#test-24-verify-slip-is-unchanged)
- [Boat Arrival Case 3](#boat-arrival-case-3)
	- [Test 25: Verify New Slip is Empty](#test-25-verify-new-slip-is-empty)
	- [Test 26: Verify Boat is Not At Sea](#test-26-verify-boat-is-not-at-sea)
	- [Test 27: Verify Boat's Current Slip](#test-27-verify-boats-current-slip)
	- [Test 28: Boat Arrival](#test-28-boat-arrival)
	- [Test 29: Verify Boat is Still Not At Sea](#test-29-verify-boat-is-still-not-at-sea)
	- [Test 30: Verify New Slip is Has Boat and URL](#test-30-verify-new-slip-is-has-boat-and-url)
	- [Test 31: Verify Old Slip is Empty](#test-31-verify-old-slip-is-empty)
- [Boat Arrival Case 4](#boat-arrival-case-4)
	- [Test : Verify New Slip is Occupied](#test-verify-new-slip-is-occupied)
	- [Test : Verify New Slip's Boat is Not At Sea](#test-verify-new-slips-boat-is-not-at-sea)
	- [Test : Verify Boat is Not At Sea](#test-verify-boat-is-not-at-sea)
	- [Test : Verify Boat's Current Slip Has This Boat](#test-verify-boats-current-slip-has-this-boat)
	- [Test : Boat Arrival Denied (403 - Slip Occupied)](#test-boat-arrival-denied-403-slip-occupied)
	- [Test : Verify New Slip is Unchanged](#test-verify-new-slip-is-unchanged)
	- [Test : Verify New Slip's Original Boat Unchanged](#test-verify-new-slips-original-boat-unchanged)
	- [Test : Verify Boat's Old Slip is Unchanged](#test-verify-boats-old-slip-is-unchanged)
	- [Test : Verify Boat is Unchanged](#test-verify-boat-is-unchanged)
- [Boat Departure](#boat-departure)
	- [Test : Verify Slip has a Boat](#test-verify-slip-has-a-boat)
	- [Test : Verify that Boat is Not At Sea](#test-verify-that-boat-is-not-at-sea)
	- [Test : Put Boat At Sea](#test-put-boat-at-sea)
	- [Test : Verify Slip Updated to Empty and Ship History Updated](#test-verify-slip-updated-to-empty-and-ship-history-updated)
	- [Test : Verify Boat Updated to At Sea](#test-verify-boat-updated-to-at-sea)
- [Delete Docked Boat](#delete-docked-boat)
	- [Test : Delete Docked Boat](#test-delete-docked-boat)
	- [Test : Check Boat Deleted](#test-check-boat-deleted)
	- [Test : Check Slip Updated when Current Boat Deleted](#test-check-slip-updated-when-current-boat-deleted)
	- [Test : Check Boat Deleted](#test-check-boat-deleted)
- [Delete Occupied Slip](#delete-occupied-slip)
	- [Test : Delete Occupied Slip](#test-delete-occupied-slip)
	- [Test : Check Slip Deleted](#test-check-slip-deleted)
	- [Test : Check Boat Updated to At Sea](#test-check-boat-updated-to-at-sea)
	- [Test :](#test-)
		- [Request](#request)
		- [Expected Response](#expected-response)

<!-- /TOC -->

## Pre-Clean
* clean datastore manually: `dev_appserver.py -c app.yaml`
* OR use a loop of GET and DELETE for boats and slips

# Boat: Read All

## Test 1: Get all boats

### Request

```
GET /boats/

```

### Expected Response

* Status is 200

* Body has an array of Empty JSON

  ```
  []
  ```
* Save `test1 = True` if this test passes, `false` otherwise

# Boat: Create & Read Boat

## Test 2: Create a new boat

### Request

* Save `test2name` as the `name` requested
* Save `test2type` as the `type` requested
* Save `test2length` as the `length` requested

```
POST /boats/

{
  "name": "Boat Name",
  "type": "Boat Type",
  "length": 10
}
```

### Expected Response

* Status is 201

* JSON that matches request data and also includes `id`, `url`, and `at_sea` set to `true`
  ```
  {
    "name": "Boat Name",
    "type": "Boat Type",
    "length": 10,
    "id": "asdfASDF1234-5678",
    "url": "http://.../boats/asdfASDF1234-5678",
    "at_sea": true
  }
  ```
* Save `test2url` as `url` given if this test passes, `null` otherwise

* Save `test2id` as `id` given if this test passes, `null` otherwise

* Save `test2response` as the JSON object if this test passes, `null` otherwise

## Test 3: URL from Test 2 Works

### Request

Verify boat was created using `url` from **Test 2**

```
GET {test2url}

```

### Expected Response

  * Status is 200

  * JSON that matches request data from **Test 2** and also includes `id` and `url` from **Test 2**, and `at_sea` is set to `true`.

  ```
  {
    "name": "Boat Name",
    "type": "Boat Type",
    "length": 10,
    "id": "asdfASDF1234-5678",
    "url": "http://.../boats/asdfASDF1234-5678",
    "at_sea": true
  }
  ```

## Test 4: ID from Test 2 Works

### Request

Verify boat was created using `id` from **Test 2**

```
GET /boats/{test2id}

```

### Expected Response

  * Status is 200

  * JSON that matches request data from **Test 2** and also includes `id` and `url` from **Test 2**, and `at_sea` is set to `true`.

  ```
  {
    "name": "Boat Name",
    "type": "Boat Type",
    "length": 10,
    "id": "asdfASDF1234-5678",
    "url": "http://.../boats/asdfASDF1234-5678",
    "at_sea": true
  }
  ```

## Test 5: Get All Boats After Test 2

### Request

Verify boat was added to list of all boats

```
GET /boats/

```

### Expected Response

* Status is 200

* If `test1 == True,` then continue with this test, otherwise fail

* Body has an array of JSON that has 1 element that matches the request data from **Test 2** and also includes `id` and `url` from **Test 2**, and `at_sea` is set to `true`.

  ```
  [
    {
      "name": "Boat Name",
      "type": "Boat Type",
      "length": 10,
      "id": "asdfASDF1234-5678",
      "url": "http://.../boats/asdfASDF1234-5678",
      "at_sea": true
    }
  ]
  ```




# Boat: Edit Boat

## Test 6: Edit Boat Name, Type, Length

### Request


* Save `test6name` as the `name` requested
* Save `test6type` as the `type` requested
* Save `test6length` as the `length` requested

```
PATCH /boats/{id}

{
  "name": "NEW Boat Name",
  "type": "NEW Type",
  "length": 20
}

```

### Expected Response

* Status is 200

* JSON that matches request data and also includes `id`, `url`, and `at_sea` set to `true`.
  ```
  {
    "name": "NEW Boat Name",
    "type": "NEW Boat Type",
    "length": 20,
    "id": "asdfASDF1234-5678",
    "url": "http://.../boats/asdfASDF1234-5678",
    "at_sea": true
  }
  ```



## Test 7: Check Boat Updated Correctly
### Request

```
GET /boats/{id}

```

### Expected Response

* Status is 200

* Body has JSON that matches the request of Test 6, includes `id`, `url`, and `at_sea` set to `true`.
  ```
  {
    "name": "NEW Boat Name",
    "type": "NEW Boat Type",
    "length": 20,
    "id": "asdfASDF1234-5678",
    "url": "http://.../boats/asdfASDF1234-5678",
    "at_sea": true
  }
  ```


# Slip: Read All Slips

## Test 8: Get all slips

### Request

```
GET /slips/

```

### Expected Response

* Status is 200

* Body has an array of Empty JSON

  ```
  []
  ```
* Save `test8 = True` if this test passes, `false` otherwise



# Slip: Create & Read Slip

## Test 9: Create a new slip

### Request

* Save `test9number` as the `number` requested

```
POST /slips/

{
  "number": 17
}
```

### Expected Response

* Status is 201

* JSON that matches request data and also includes autogenerated `id` and `url`, as well as default values for `current_boat` (`null`), `current_boat_url` (`null`), `arrival_date` (`null`), and `departure_history`  (empty array `[]`)
	```
	{           
		"number": 17,                
		"current_boat": null,
		"current_boat_url": null,  
		"arrival_date": null,  
		"departure_history": [],
		"id": "asdfASDF1234-1111",
		"url": "http://.../slips/asdfASDF1234-1111"
	}
	```
* Save `test9url` as `url` given if this test passes, `null` otherwise

* Save `test9id` as `id` given if this test passes, `null` otherwise

* Save `test9response` as the JSON object if this test passes, `null` otherwise


## Test 10: URL from Test 9 Works

### Request

Verify slip was created using `url` from **Test 9**

```
GET {test9url}

```

### Expected Response

  * Status is 200

  * JSON that matches request data from **Test 9** and also includes `id` and `url` from **Test 9**. Response has default values for `current_boat` (`null`), `current_boat_url` (`null`), `arrival_date` (`null`), and `departure_history`  (empty array `[]`).

  ```
	{           
	  "number": 17,                
	  "current_boat": null,   
		"current_boat_url": null,  
	  "arrival_date": null,  
	  "departure_history": [],
	  "id": "asdfASDF1234-1111",
	  "url": "http://.../slips/asdfASDF1234-1111"
  }
  ```

## Test 11: ID from Test 9 Works

### Request

Verify slip was created using `id` from **Test 9**

```
GET /slips/{test9id}

```

### Expected Response

  * Status is 200

  * JSON that matches request data from **Test 9** and also includes `id` and `url` from **Test 9**. Response has default values for `current_boat` (`null`), `current_boat_url` (`null`), `arrival_date` (`null`), and `departure_history`  (empty array `[]`).

	```
	{           
	  "number": 17,                
	  "current_boat": null,  
		"current_boat_url": null,   
	  "arrival_date": null,  
	  "departure_history": [],
	  "id": "asdfASDF1234-1111",
	  "url": "http://.../slips/asdfASDF1234-1111"
  }
  ```

## Test 12: Get All Slips After Test 9

### Request

Verify slip was added to list of all slips

```
GET /slips/

```

### Expected Response

* Status is 200

* If `test8 == True,` then continue with this test, otherwise fail

* Body has an array of JSON that has 1 element that matches the request data from **Test 9** and also includes `id` and `url` from **Test 9**. Response has default values for `current_boat` (`null`), `current_boat_url` (`null`), `arrival_date` (`null`), and `departure_history`  (empty array `[]`).

  ```
  [
		{           
			"number": 17,                
			"current_boat": null,   
			"current_boat_url": null,    
			"arrival_date": null,  
			"departure_history": [],
			"id": "asdfASDF1234-1111",
			"url": "http://.../slips/asdfASDF1234-1111"
		}
  ]
  ```


# Slip: Edit Slip
## Test 13: Edit Slip Number

### Request

```
PATCH /slips/{test9id}

{
  "number": 38
}

```

### Expected Response

* Status is 200

* JSON that matches request data changes and the rest of the slip is unchanged (check against `test9response`).

  ```
	{           
		"number": 38,                
		"current_boat": null,   
		"current_boat_url": null,    
		"arrival_date": null,  
		"departure_history": [],
		"id": "asdfASDF1234-1111",
		"url": "http://.../slips/asdfASDF1234-1111"
	}
  ```

## Test 14: Check Slip Number Updated Correctly

### Request

```
GET /slips/{test9id}

```

### Expected Response

* Status is 200

* Body has JSON that matches the request of Test 13 and the rest of the slip is unchanged (check against `test9response`).

	```
	{           
		"number": 38,                
		"current_boat": null,   
		"current_boat_url": null,    
		"arrival_date": null,  
		"departure_history": [],
		"id": "asdfASDF1234-1111",
		"url": "http://.../slips/asdfASDF1234-1111"
	}
	```



# Boat Arrival Case 1

Place an at sea boat into an empty slip.

## Test 15: Verify Slip is Empty

### Request

```
GET /slips/{test9id}

```

### Expected Response
* Status is 200

* JSON that has `id` that matches the requested value. JSON has `current_boat` is `null`, `current_boat_url` is `null`, and `arrival_date` is `null`.


```
{           
	"number": 17,                
	"current_boat": null,  
	"current_boat_url": null,   
	"arrival_date": null,  
	"departure_history": [],
	"id": "asdfASDF1234-1111",
	"url": "http://.../slips/asdfASDF1234-1111"
}
```
* Save `test15slip` with the JSON slip response.


## Test 16: Verify Boat is At Sea

### Request

Verify boat is at sea.

```
GET /boats/{test2id}

```

### Expected Response

* Status is 200

* JSON that has `id` that matches the requested value. JSON has `at_sea` equal to `true`.

```
{
  "name": "NEW Boat Name",
  "type": "NEW Boat Type",
  "length": 20,
  "id": "asdfASDF1234-5678",
  "url": "http://.../boats/asdfASDF1234-5678",
  "at_sea": true
}
```

* Save `test16boat` with the JSON boat response.


## Test 17: Boat Arrival

### Request

* Save `test17arrival_date` for future use.

```
PUT /boats/{test2id}/slips/{test9id}

{
	"arrival_date", "1/15/2016"
}
```

### Expected Response

* Status is 204

* No Content


## Test 18: Verify Boat is Not at Sea

### Request

Verify boat is not at sea.

```
GET /boats/{test2id}

```

### Expected Response

  * Status is 200

  * JSON that matches `test16boat` except for `at_sea` is equal to `false`.

  ```
  {
    "name": "NEW Boat Name",
    "type": "NEW Boat Type",
    "length": 20,
    "id": "asdfASDF1234-5678",
    "url": "http://.../boats/asdfASDF1234-5678",
    "at_sea": false
  }
  ```
* Save `test18 = true` if test passes, `false` otherwise.

* Save `test18response` as JSON of response.

## Test 19: Verify Slip lists the Boat and URL

### Request

```
GET /slips/{test9id}

```

### Expected Response
* Status is 200

* JSON that that matches `test15slip` except for `current_boat` is equal to `id` of `test16boat`, `current_boat_url` is equal to `url` of `test16boat`, and `arrival_date` matches requested date (`test17arrival_date`).

```
{           
	"number": 17,                
	"current_boat": "asdfASDF1234-5678",  
	"current_boat_url": "http://.../boats/asdfASDF1234-5678",   
	"arrival_date": "1/15/2016",  
	"departure_history": [],
	"id": "asdfASDF1234-1111",
	"url": "http://.../slips/asdfASDF1234-1111"
}
```
* Save `test19 = true` if test passes, `false` otherwise.

* Save `test19response` as JSON of response.


# Boat Departure

* If `test18 == true` and `test19 == true`, then continue with this group of tests, otherwise fail. (That is, Boat is Not At Sea and Slip has the Boat.)


## Test 20: Boat Departs Slip

### Request

* If `test18 == true` and `test19 == true`, then continue with this test, otherwise fail. (That is, Boat is Not At Sea and Slip has the Boat.)

* Save `test20departure_date` for future use.

```
DELETE /boats/{test2id}/slips/{test9id}

{
	"departure_date": "2/1/2016"
}

```

### Expected Response

* Status is 204

* No Content


## Test 21: Verify Slip is Empty and Departure History is Updated

### Request

Verify slip is empty, and departure_history Updated. Compare with boat from `test19response`.

```
GET /slips/{test9id}

```

### Expected Response

* Status is 200

* JSON that matches `test19response`, except `current_boat` (`null`), `current_boat_url` (`null`), `arrival_date` (`null`).

* Verify `departure_history` is the same as that in `test19response` except for the addition of the `current_boat` from `test19response` and the `departure_date` from `test20departure_date`.

```
{           
  "number": 17,                
  "current_boat": null,  
	"current_boat_url": null,   
  "arrival_date": null,  
  "departure_history": [
		{"departure_date": "2/1/2016", "departed_boat": "asdfASDF1234-5678"}
	],
  "id": "asdfASDF1234-1111",
  "url": "http://.../slips/asdfASDF1234-1111"
}
```

## Test 22: Verify Boat Updated to At Sea

### Request

Verify boat is at sea and unchanged otherwise.

```
GET /boats/{test2id}

```

### Expected Response

* Status is 200

* JSON that matches `test18response`, except `at_sea = true`.

```
{
  "name": "NEW Boat Name",
  "type": "NEW Boat Type",
  "length": 20,
  "id": "asdfASDF1234-5678",
  "url": "http://.../boats/asdfASDF1234-5678",
  "at_sea": true
}
```







# Boat Arrival Case 2

Try to place an at sea boat into an occupied slip and get denied. No changes.

## Test 20: Verify Slip is Occupied

## Test 21: Verify Boat is At Sea

## Test 22: Boat Arrival Denied (403 - Slip Occupied)

## Test 23: Verify Boat is Unchanged

## Test 24: Verify Slip is Unchanged


# Boat Arrival Case 3

Move a docked boat into an empty slip.

## Test 25: Verify New Slip is Empty

## Test 26: Verify Boat is Not At Sea

## Test 27: Verify Boat's Current Slip

## Test 28: Boat Arrival

## Test 29: Verify Boat is Still Not At Sea

## Test 30: Verify New Slip is Has Boat and URL

## Test 31: Verify Old Slip is Empty


# Boat Arrival Case 4

Try to place a docked boat into an occupied slip and get denied. No changes.

## Test : Verify New Slip is Occupied By Another

## Test : Verify New Slip's Boat is Not At Sea

## Test : Verify Boat is Not At Sea

## Test : Verify Boat's Current Slip Has This Boat

## Test : Boat Arrival Denied (403 - Slip Occupied)

## Test : Verify New Slip is Unchanged

## Test : Verify New Slip's Original Boat Unchanged

## Test : Verify Boat's Old Slip is Unchanged

## Test : Verify Boat is Unchanged



# Delete Docked Boat

## Test : Delete Docked Boat

## Test : Check Boat Deleted

## Test : Check Slip Updated when Current Boat Deleted

## Test : Check Boat Deleted



# Delete Occupied Slip

## Test : Delete Occupied Slip

## Test : Check Slip Deleted

## Test : Check Boat Updated to At Sea
