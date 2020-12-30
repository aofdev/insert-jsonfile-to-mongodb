# insert-jsonfile-to-mongodb

A support parsing field DateTime insert field type date in MongoDB.

| Argument         | Description                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------- |
| mongo_uri        | a URI which can be used to connect a Mongo. example `mongodb://root:root!@localhost:27017/` |
| mongo_db         | Mongo Database example `testdb`                                                             |
| mongo_collection | Mongo Collection example `test_collection`                                                  |
| jsonfile         | a path json file                                                                            |

## Example

```sh
docker run --rm -it -v $(pwd):/tmp aofdev/insert-jsonfile-to-mongodb:latest bash -c "python main.py --mongo_uri='mongodb://root:!@localhost:27017/?authSource=admin' --mongo_db='testdb' --mongo_collection='test_collection' --jsonfile='/tmp/example/test_data.json'"
```
