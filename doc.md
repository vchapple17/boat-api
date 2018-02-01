# boat-api

Valerie Chapple

## Boat Example JSON

| Name | Type | Description |
|--------|----------|---------|
| `url` | `string` | **Required.** URL with auto-generated unique id |
| `id` | `string` | **Required.** Auto-generated unique id |
| `name` | `string` | **Required.** Name of boat |
| `type` | `string` | **Required.** Type of boat |
| `length` | `int` | **Required.** Length of boat in feet|
| `at_sea` | `boolean` | **Required.** Default is `false`|

```
{
  "url": "https://totemic-splicer-145122.appspot.com/boats/kj0987a234bcdasdf12",
  "id":"kj0987a234bcdasdf12",        
  "name": "Sea Witch",  
  "type":"Catamaran",   
  "length":28,          
  "at_sea":false        
}
```

## Slip Example JSON

| Name | Type | Description |
|--------|----------|---------|
| `url` | `string` | **Required.** URL with auto-generated unique id |
| `id` | `string` | **Required.** Auto-generated unique id |
| `number` | `int` | **Required.** Slip number; may not be unique|
| `current_boat` | `string` | ID of the current boat, null if empty |
| `current_boat_url` | `string` | Unique URL of the current boat, null if empty |
| `arrival_date` | `string` | Date current boat arrived in "MM/DD/YYYY", null if empty  |
| `departure_history` | `[ histJSON ]` | list of previous boats and departure dates |


A `histJSON` is a json object that contains the `departure_date` and the ID of the `departed_boat`.

```
{
  "url": "https://totemic-splicer-145122.appspot.com/slips/123abc",
  "id":"123abc",              
  "number": 5,                
  "current_boat":"abc555",    
  "current_boat_url":"https://totemic-splicer-145122.appspot.com/boats/abc555",
  "arrival_date":"1/1/2015",  
  "departure_history":        
    [ { "departure_date":"11/4/2014", "departed_boat":"123aaa" } ]  
}
```


## View a list of boats

Returns an array of boat information in JSON, including urls to each boat.

```
GET /boats
```

**Response**

```
Status: 200 OK

[
  {
    "url": "https://totemic-splicer-145122.appspot.com/boats/cdasdf12kj0987a23",
    "id": "cdasdf12kj0987a23",
    "name": "S.S. Awesome",
    "type": "power boat",
    "length": 18,          
    "at_sea": false
  }
]
```

## View a single boat

Returns information of a boat with `{boat_id}` in JSON, including the url to the boat.

```
GET /boats/{boat_id}
```

**Response**
```
Status: 200 OK

{
  "url": "https://totemic-splicer-145122.appspot.com/boats/kj0987a234bcdasdf15",
  "id": "kj0987a234bcdasdf15",
  "name": "S.S. Awesome",
  "type": "power boat",
  "length": 18,          
  "at_sea": false
}
```

## View a list of slips

Returns an array of slip information in JSON, including urls to each slip.

```
GET /slips
```

**Response**

```
Status: 200 OK

[
  {
    "url": "https://totemic-splicer-145122.appspot.com/slips/cdasdf12kj0987a23",
    "id":"cdasdf12kj0987a23",
    "number": 5,
    "current_boat":"kj0987a234bcdasdf1234hl",
    "current_boat_url":"https://totemic-splicer-145122.appspot.com/boats/kj0987a234bcdasdf1234hl",
    "arrival_date":"1/1/2015",
    "departure_history":
      [ {
        "departure_date":"11/4/2014",
        "departed_boat":"123aaa"
        }, ...
      ]  
  }
]
```

## View a single slip

Returns information of a slip with `{slip_id}` in JSON, including the url to the slip.

```
GET /slips/{slip_id}
```

**Response**
```
Status: 200 OK

{
  "url": "https://totemic-splicer-145122.appspot.com/slips/123abc",
  "id":"123abc",
  "number": 5,
  "current_boat":"abc555",
  "current_boat_url":"https://totemic-splicer-145122.appspot.com/boats/abc555",
  "arrival_date":"1/1/2015",
  "departure_history":
    [ {
      "departure_date":"11/4/2014",
      "departed_boat":"123aaa"
      }, ...
    ]
}
```


## Create a new boat

```
POST /boats
```
**Input**

| Name | Type | Description |
|--------|----------|---------|
| `name` | `string` | **Required.** Name of boat |
| `type` | `string` | **Required.** Type of boat |
| `length` | `int` | **Required.** Length of boat in feet|

Invalid data, extra data, or incorrect data types will be rejected.

**Note**: A new boat defaults to `true` for `at sea`, and the boat `id` is auto-generated on the server.

**Request Body**

```
{
  "name": "Escape",
  "type": "yacht",
  "length": 390
}
```

**Response**
```
Status: 201 Created

{
  "url": "https://totemic-splicer-145122.appspot.com/boats/dasdf1234hl",
  "id": "dasdf1234hl",
  "name": "Escape",
  "type": "yacht",
  "length": 390,
  "at sea": true
}
```

## Create a new slip

```
POST /slips
```
**Input**

| Name | Type | Description |
|--------|----------|---------|
| `number` | `int` | **Required.** Slip number; may not be unique|

Invalid data, extra data, or incorrect data types will be rejected.

**Note 1**: A new slip defaults to being empty. That is, `current_boat` and `arrival_date` default to `null`, and the `departure_history` is an empty array.

**Note 2**: The slip `id` is auto-generated on the server.

**Request Body**

```
{
  "number": 125
}
```

**Response**
```
Status: 201 Created

{
  "url": "https://totemic-splicer-145122.appspot.com/slips/456abc",
  "id":"456abc",
  "number": 125,
  "current_boat":"kj0987a234bcdasdf15",
  "current_boat_url":"https://totemic-splicer-145122.appspot.com/boats/kj0987a234bcdasdf15",
  "arrival_date":"1/1/2015",
  "departure_history":
    [ {
      "departure_date":"11/4/2014",
      "departed_boat":"87a234bcdailkjsdf15"
      }, ...
    ]  
}
```

## Edit a boat

```
PATCH /boats/{boat_id}
```
**Input**

| Name | Type | Description |
|--------|----------|---------|
| `name` | `string` | **Required.** Name of boat |
| `type` | `string` | **Required.** Type of boat |
| `length` | `int` | **Required.** Length of boat in feet|

Invalid data, extra data, or incorrect data types will be rejected.

**Note**: The property `at sea` can only be changed by docking or departing a boat.

**Request Body**

```
{
  "name": "Escape",
  "type": "yacht",
  "length": 390
}
```

**Response**
```
Status: 200 OK

{
  "url": "https://totemic-splicer-145122.appspot.com/boats/dasdf1234hl",
  "id": "dasdf1234hl",
  "name": "Escape",
  "type": "yacht",
  "length": 390,
  "at sea": true
}
```



## Edit a slip

```
PATCH /slips/{slip_id}
```
**Input**

| Name | Type | Description |
|--------|----------|---------|
| `number` | `int` | **Required.** Slip number; may not be unique|

Invalid data, extra data, or incorrect data types will be rejected.

**Note**: All other slip properties can only be changed by docking or departing a boat.

**Request Body**

```
{
  "number": 1250
}
```

**Response**
```
Status: 200 OK

{
  "url": "https://totemic-splicer-145122.appspot.com/slips/456abc",
  "id": "456abc",
  "number": 1250,
  "current_boat": null,
  "current_boat_url": null,
  "arrival_date": null,
  "departure_history":
    [ {
      "departure_date":"11/4/2014",
      "departed_boat":"87a234bcdailkjsdf15"
      }, ...
    ]  
}
```


## Delete a boat

```
DELETE /boats/{boat_id}
```
**Response**
```
Status: 204 No Content
```
Boat is removed from data store. If the boat was current not at sea, then the slip is emptied through the data store.

## Delete a slip

```
DELETE /slips/{slip_id}
```

**Response**
```
Status: 204 No Content
```
Slip is removed from data store. If the slip is currently occupied, the boat is put to sea.

## Set a Boat to a slip
```
PUT /boats/{boat_id}/slips/{slip_id}
```

Request will be rejected if the boat is already docked or the slip is already occupied.

**Request Body**
```
{
	"arrival_date", "1/15/2016"
}
```

**Response**
```
Status: 204 No Content
```

## Set a Boat to Sea

```
DELETE /boats/{boat_id}/slips/{slip_id}?departure={datestring}
```

* The `boat_id` and date of `departure` from the slip is appended to the slip's `departure_history` array.
* The slip's properties of `current_boat`, `current_boat_url`, and `arrival_date` are set to `null`.
* The parameter `departure` must be a date string in the form of `mm/dd/yyyy`, such as `2/5/2016`
* Request will be rejected if the boat is already docked or the slip is already occupied.


**Response**
```
Status: 204 No Content
```
