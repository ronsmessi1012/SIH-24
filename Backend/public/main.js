document.addEventListener('DOMContentLoaded', () => {
    // Initialize Leaflet map
    const map = L.map('map').setView([48.235416, 8.340875], 13); // Set a default center and zoom level

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);

    // Sample waypoints
    const waypoints = [
        [48.235416, 8.340875], // Start location
        [48.233571, 8.344171]  // End location
    ];

    // Fetch route from the server
    fetch(`/optimize-route?waypoints=${encodeURIComponent(JSON.stringify(waypoints))}`)
        .then(response => response.json())
        .then(data => {
            if (data.routes && data.routes.length > 0) {
                // Extract the route coordinates
                const route = data.routes[0].geometry.coordinates.map(coord => [coord[1], coord[0]]); // Convert [lng, lat] to [lat, lng]
                
                // Add the route to the map
                const polyline = L.polyline(route, {
                    color: 'blue',
                    weight: 5,
                    opacity: 0.7,
                    dashArray: '5, 10'
                }).addTo(map);

                // Add markers for waypoints
                data.waypoints.forEach((waypoint, index) => {
                    L.marker([waypoint.location[1], waypoint.location[0]], {
                        title: waypoint.name || `Waypoint ${index + 1}`
                    }).addTo(map)
                    .bindPopup(waypoint.name || `Waypoint ${index + 1}`);
                });

                // Fit the map to the bounds of the route
                const routeBounds = polyline.getBounds();
                map.fitBounds(routeBounds);
            }
        })
        .catch(error => console.error('Error:', error));
});
