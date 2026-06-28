import express from 'express';
import fetch from 'node-fetch';
import path from 'path';
import { exec } from 'child_process';
import { promisify } from 'util';

const execPromise = promisify(exec);
const app = express();
const PORT = 3000;

// Serve static files from 'public'
app.use(express.static('public'));

// Endpoint for route optimization
app.get('/optimize-route', async (req, res) => {
  const { waypoints } = req.query;

  if (!waypoints) {
    return res.status(400).json({ error: 'Waypoints parameter is required' });
  }

  try {
    const decodedWaypoints = decodeURIComponent(waypoints);
    const coordinates = JSON.parse(decodedWaypoints);

    // Convert coordinates to string format suitable for Python
    const coordinatesString = JSON.stringify(coordinates);

    // Construct the command to run the Python script
    const pythonScriptPath = path.join(process.cwd(), 'optimize_route.py');
    const command = `python ${pythonScriptPath} '${coordinatesString}'`;

    // Execute the Python script
    const { stdout, stderr } = await execPromise(command);

    if (stderr) {
      console.error(`Error executing Python script: ${stderr}`);
      return res.status(500).send('Error executing Python script');
    }

    try {
      // Parse and return the result from Python script
      const result = JSON.parse(stdout);
      res.json(result);
    } catch (parseError) {
      console.error(`Error parsing Python script output: ${parseError}`);
      res.status(500).send('Error parsing Python script output');
    }
  } catch (parseError) {
    console.error(`Error parsing waypoints: ${parseError}`);
    res.status(400).send('Invalid JSON format for waypoints');
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
