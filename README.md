# Minecraft Geometry Decryptor

## Instructions on How to Use the Decryptor

1. **Requirements**:
   - Ensure you have [Java JDK](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) installed.
   - You will need Maven to build the project: [Maven Installation Guide](https://maven.apache.org/install.html) 

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/Piachenya/minecraft-geometry-decryptor.git
   cd minecraft-geometry-decryptor
   ```

3. **Build the Project**:
   ```bash
   mvn clean package
   ```
   This will create an executable jar file in the `target` directory.

4. **Run the Decryptor**:
   Once the build is successful, you can run the decryptor using:
   ```bash
   java -jar target/your-jar-file.jar
   ```
   Replace `your-jar-file.jar` with the actual jar file name created in the target directory.

## Building an EXE

To build an EXE from the jar file, you can use [Launch4j](http://launch4j.sourceforge.net/):

1. Download and set up Launch4j.
2. Point it to your jar file and configure the required parameters.
3. Build the EXE.

## Further Information

Check the project documentation for any additional instructions or troubleshooting tips.
Good luck!