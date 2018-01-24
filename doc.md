# boat-api

<!-- CS496 api structure -->
<!-- https://developer.github.com/v3/gists/#input -->

## Boat Example JSON

| Name | Type | Description |
|--------|----------|---------|
| `id` | `string` | **Required.** Auto-generated unique id |
| `name` | `string` | **Required.** Name of boat |
| `type` | `string` | **Required.** Type of boat |
| `length` | `int` | **Required.** Length of boat in feet|
| `at_sea` | `boolean` | **Required.** Default `false`|

```
{ "id":"abc123",        
  "name": "Sea Witch",  
  "type":"Catamaran",   
  "length":28,          
  "at_sea":false        
}
```

## Slip Example JSON

| Name | Type | Description |
|--------|----------|---------|
| `id` | `string` | **Required.** Auto-generated unique id |
| `number` | `int` | **Required.** Slip number; may not be unique|
| `current_boat` | `string` | ID of the current boat, null if empty |
| `arrival_date` | `string` | Date current boat arrived in "MM/DD/YYYY", null if empty  |
| `departure_history` | `[ histObj ]` | list of previous boats and departure dates |


A `histObj` is a json object that contains the `departure_date` and the ID of the `departed_boat`.

```
{ "id":"123abc",              
  "number": 5,                
  "current_boat":"abc555",    
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
    "url": "https://totemic-splicer-145122.appspot.com/boats/asdf1234hlkj0987a",
    "id": "asdf1234hlkj0987a",
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
  "url": "https://totemic-splicer-145122.appspot.com/boats/asdf1234hlkj0987a",
  "id": "asdf1234hlkj0987a",
  "name": "S.S. Awesome",
  "type": "power boat",
  "length": 18,          
  "at_sea": false
}
```

## View a list of slips

Returns an array of slip information in JSON, including urls to each slp.

```
GET /slips
```

**Response**
```
Status: 200 OK

[
  {
    "url": "https://totemic-splicer-145122.appspot.com/slips/123abc",
    "id":"123abc",
    "number": 5,
    "current_boat":"abc555",
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

<!-- ## View the current boat in a slip

Return the URL to the boat the currently occupies the slip.

```
GET /slips/{slip_id}/boat
```

**Response**
```
Status: 200 OK

{
  "url":



}
``` -->

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


```
{
  "name": "S.S. Brighteyes",
  "type": "canoe",
  "length": 10
}
```

**Response**
```
Status: 201 Created

{
  "name": "S.S. Brighteyes",
  "type": "canoe",
  "length": 10
}
```


???ERROR???
```
Status:

{
  "url":


}
```



## Create a new slip

## Edit a boat

## Edit a slip

## Delete a boat

## Delete a slip

## Set a boat to sea

## Set a boat to a slip

## E.C.
