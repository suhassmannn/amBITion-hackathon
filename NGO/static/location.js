// window.onload = function() {
//     getLocation();
// };

// function getLocation() {
//     if (navigator.geolocation) {
//         // Ask for permission and get the user's location
//         navigator.geolocation.getCurrentPosition(showPosition, showError);
//     } else {
//         alert("Geolocation is not supported by this browser.");
//     }
// }

// function showPosition(position) {
//     const latitude = position.coords.latitude;
//     const longitude = position.coords.longitude;

//     console.log("Latitude: " + latitude + "\nLongitude: " + longitude);

//     getCityLocation(latitude, longitude);
// }

// function showError(error) {
//     switch(error.code) {
//         case error.PERMISSION_DENIED:
//             alert("User denied the request for Geolocation.");
//             break;
//         case error.POSITION_UNAVAILABLE:
//             alert("Location information is unavailable.");
//             break;
//         case error.TIMEOUT:
//             alert("The request to get user location timed out.");
//             break;
//         case error.UNKNOWN_ERROR:
//             alert("An unknown error occurred.");
//             break;
//     }
// }

// function getCityLocation(lat, lng) {
//     const apiKey = 'febcc609477c4e2d9660f3c89eb051c6'; // Replace with your OpenCage API key
//     const url = "https://api.opencagedata.com/geocode/v1/json?q=${lat}+${lng}&key=${apiKey}";

//     fetch(url)
//         .then(response => response.json())
//         .then(data => {
//             if (data.results && data.results.length > 0) {
//                 const city = data.results[0].components.city || data.results[0].components.town || data.results[0].components.village || 'Unknown location';
//                 console.log("City: " + city);

//                 // Send the location data to Django
//                 sendLocationToDjango(lat, lng, city);
//             } else {
//                 console.log("No results found");
//             }
//         })
//         .catch(error => {
//             console.error("Error fetching city location:", error);
//         });
// }

// function sendLocationToDjango(lat, lng, city) {
//     fetch('/receive-location/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded',
//             'X-CSRFToken': getCookie('csrftoken')
//         },
//         body: latitude=${lat}&longitude=${lng}&city=${city}
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Response from Django:', data);
//     })
//     .catch(error => {
//         console.error('Error sending location data to Django:', error);
//     });
// }

// // Function to get CSRF token from cookies
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
