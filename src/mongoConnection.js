const { MongoClient, ServerApiVersion } = require('mongodb');

const uri = process.env.MONGODB_URI;
if (!uri) {
  throw new Error('Missing MONGODB_URI environment variable. Set it before running your app.');
}

const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  },
});

async function connectMongo() {
  await client.connect();
  return client;
}

async function getDatabase(dbName = process.env.MONGO_DB_NAME || 'test') {
  const mongoClient = await connectMongo();
  return mongoClient.db(dbName);
}

async function closeMongo() {
  await client.close();
}

module.exports = {
  connectMongo,
  getDatabase,
  closeMongo,
};
