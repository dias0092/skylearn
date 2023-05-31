$(document).ready(function() {
    const weatherAPIKey = '38ee7397971144a19aa64321232505';
    const countryAPIURL = 'https://restcountries.com/v3.1/name/';
    const weatherAPIURL = 'https://api.weatherapi.com/v1/current.json?q=';
  
    const countryDetails = $('#country-details');
    const weatherDetails = $('#weather-details');
  
    // Event listener for form submission
    $('#search-form').submit(async function(event) {
      event.preventDefault();
  
      const country = $('#country-input').val().trim();
  
      if (country !== '') {
        await getCountryInformation(country);
      }
    });
  
    // Function to fetch and display country information
    async function getCountryInformation(country) {
      try {
        // Fetch country information using the provided country name
        const response = await fetch(`${countryAPIURL}${country}`);
        const data = await response.json();
  
        const countryData = data[0];
        const flagURL = countryData.flags.svg;
        const currencies = countryData.currencies;
        const currencyCode = Object.keys(currencies)[0];
        const currencyName = currencies[currencyCode].name;
        const currencySymbol = currencies[currencyCode].symbol;
        const capitalCity = countryData.capital[0];
        const nativeName = countryData.name.nativeName[Object.keys(countryData.name.nativeName)[0]].official;
        const countryName = countryData.name.common;
        const wikiPageURL = `https://en.wikipedia.org/wiki/${countryName}`;
  
        const currencyInfo = `${currencyCode} (${currencyName}, ${currencySymbol})`;
  
        const locationDetails = `${countryData.name.common}, ${countryData.region}, ${countryData.subregion}`;
  
        // Fetch weather information using the capital city of the country
        const weatherResponse = await fetch(`${weatherAPIURL}${countryData.capital[0]}&key=${weatherAPIKey}`);
        const weatherData = await weatherResponse.json();
  
        const weatherDescription = weatherData.current.condition.icon;
        const temperature = weatherData.current.temp_c;
  
        // Generate HTML for displaying country details
        const countryDetailsHTML = `
          <div class="card border-0">
          <img src="${flagURL}" alt="Flag of ${countryName}" class="card-img-top">
            <div class="card-body">
              <h2 class="card-title text-center text-capitalize">${countryName}</h2>
              <ul class="list-group list-group-flush">
                <li class="list-group-item"><strong>Native Name:</strong> ${nativeName}</li>
                <li class="list-group-item"><strong>Primary Currency:</strong> ${currencyInfo}</li>
                <li class="list-group-item"><strong>Location:</strong> ${locationDetails}</li>
                <li class="list-group-item"><strong>Capital City:</strong> ${capitalCity}</li>
                <li class="list-group-item"><button type="submit" class="btn btn-primary" id="wikipedia-button" data-url="${wikiPageURL}">Info</button>
  </li>
              </ul>
            </div>
          </div>
          `;
        // Generate HTML for displaying weather details
        const weatherDetailsHTML = `
  <div class="card mt-5">
    <div class="weather-icon-wrapper">
      <img src="${weatherDescription}" alt="Weather Icon" class="weather-icon">
    </div>
    <div class="card-body text-center">
      <h2 class="card-title temperature">${temperature}°C</h2>
      <h3 class="card-subtitle text-muted">${capitalCity}</h3>
    </div>
  </div>
        `;
  
        countryDetails.html(countryDetailsHTML);
        weatherDetails.html(weatherDetailsHTML);
      } catch (error) {
        countryDetails.html('<p class="text-danger">Failed to retrieve country information. Please try again.</p>');
        weatherDetails.html('<p class="text-danger">Failed to retrieve weather information. Please try again.</p>');
      }
    }
  
  
  });
  $(document).on('click', '#wikipedia-button', function() {
    const wikiURL = $(this).data('url');
    window.open(wikiURL, '_blank');
  });