import asyncio
import db
import embeddings

data = [
    {"title": "The importance of Unit Testing", "body": "Unit testing ensures that individual components of software work as expected. It increases code confidence."},
    {"title": "Test Driven Development", "body": "TDD is a software development process relying on software requirements being converted to test cases before software is fully developed."},
    {"title": "Mocking in Python", "body": "Mocking allows you to replace parts of your system under test and simulate their behavior. Essential for isolation."},
    {"title": "Code Coverage Metrics", "body": "Code coverage determines how much of your source code is executed when the test suite runs. It helps find untested paths."},
    {"title": "Integration Testing vs Unit Testing", "body": "While unit tests check individual modules, integration tests verify that different modules or services work well together."},
    
    {"title": "Introduction to Vector Search", "body": "Vector search allows for semantic similarity search by converting text into dense vectors. It understands context better than keywords."},
    {"title": "How pgvector works", "body": "pgvector is a PostgreSQL extension that stores vectors and performs similarity searches using distance metrics like cosine similarity."},
    {"title": "Embeddings in NLP", "body": "Embeddings are vector representations of words or documents. Similar concepts are mapped close to each other in vector space."},
    {"title": "Cosine Similarity", "body": "Cosine similarity measures the cosine of the angle between two vectors. It is often used to determine how similar two documents are."},
    {"title": "HNSW Indexing", "body": "Hierarchical Navigable Small World graphs are used for efficient approximate nearest neighbor search in high-dimensional spaces."},
    
    {"title": "Renewable Energy Sources", "body": "Renewable energy comes from sources that are naturally replenished, such as sunlight, wind, and rain."},
    {"title": "Solar Power Efficiency", "body": "Improving the efficiency of solar panels allows for more energy capture from the same surface area. Photovoltaic cells are key."},
    {"title": "Wind Energy challenges", "body": "Wind energy is clean but intermittent. Energy storage solutions are required to manage supply and demand fluctuations."},
    {"title": "Hydropower systems", "body": "Hydropower generates electricity by using the energy of moving water. It is one of the oldest renewable energy sources."},
    {"title": "Geothermal Energy", "body": "Geothermal energy harnesses heat from within the earth. It provides a constant and reliable source of power."},

    {"title": "Web Performance Optimization", "body": "Optimizing web performance involves reducing load times and improving responsiveness. Techniques include minification and caching."},
    {"title": "Lazy Loading Images", "body": "Lazy loading defers the loading of non-critical resources like images until they are needed, improving initial page load time."},
    {"title": "Critical Rendering Path", "body": "The critical rendering path is the sequence of steps the browser goes through to convert HTML, CSS, and JS into pixels on the screen."},
    {"title": "Browser Caching Strategies", "body": "Effective caching strategies can significantly reduce server load and improve speed for returning users by storing assets locally."},
    {"title": "Minimizing JavaScript Blocking", "body": "Large JavaScript files can block the main thread. Breaking them up or loading them asynchronously improves interactivity."}
]

async def seed():
    print("Initializing DB...")
    await db.init_db()
    
    print("Seeding data...")
    for item in data:
        print(f"Processing: {item['title']}")
        emb = embeddings.generate_embedding(item['title'] + " " + item['body'])
        await db.insert_document(item['title'], item['body'], emb)
        
    print("Seeding complete!")

if __name__ == "__main__":
    asyncio.run(seed())
