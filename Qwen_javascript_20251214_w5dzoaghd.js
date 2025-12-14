import * as Location from 'expo-location';

useEffect(() => {
  (async () => {
    let { status } = await Location.requestForegroundPermissionsAsync();
    if (status !== 'granted') return;

    let location = await Location.getCurrentPositionAsync({});
    const { latitude, longitude } = location.coords;

    const res = await fetch(`${API_URL}/supermercados/proximos?lat=${latitude}&lng=${longitude}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    const data = await res.json();
    setSupermercados(data);
  })();
}, []);