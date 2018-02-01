# Boat API

# Setup

## Local

Install and set up Google Cloud SDK locally [https://cloud.google.com/sdk/downloads]. 

## Google Cloud

After you create your project and register it through Google, you can easily upload files and deploy apps using the Google Cloud Shell.[https://console.cloud.google.com/home/dashboard]

# Deployment
To deploy your app for testing and development:

```
dev_appserver.py app.yaml
```

To deploy the app for testing and development with a clean datastore:

```
dev_appserver.py --clear_datastore=yes app.yaml
```

To deploy the app to a server using Google Cloud Shell:
```
gcloud app deploy app.yaml
```

# Endpoints

## Boat

```
GET /boats/
POST /boats/

GET /bosts/{boat_id}
PATCH /bosts/{boat_id}
DELETE /bosts/{boat_id}
```

## Slip

```
GET /slips/
POST /slips/

GET /slips/{slip_id}
PATCH /slips/{slip_id}
```

## Docking & Removing Boats

```
PUT /boats/{boat_id}/slips/{slip_id}
DELETE /boats/{boat_id}/slips/{slip_id}
```
