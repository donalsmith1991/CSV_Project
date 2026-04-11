const { getDatabase, closeMongo } = require('./mongoConnection');

async function main() {
  try {
    const dbName = process.env.MONGO_DB_NAME || 'test';
    const collectionName = process.env.MONGO_COLLECTION || 'sample_collection';
    const db = await getDatabase(dbName);

    const collection = db.collection(collectionName);
    const count = await collection.countDocuments({});
    const collections = await db.listCollections().toArray();

    console.log(`Connected to database '${dbName}' and collection '${collectionName}'.`);
    console.log(`Document count: ${count}`);
    console.log('Available collections:', collections.map((c) => c.name).join(', '));
  } catch (error) {
    console.error('MongoDB connection failed:', error);
  } finally {
    await closeMongo();
  }
}

main();
