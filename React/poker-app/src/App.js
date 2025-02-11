import React, {useState, useEffect, use} from 'react';
import api from './api';

const App = () => {
  const [buyin, setBuyin] = useState([]);
  const [formData, setFormData] = useState({
    name: '',
    buyin: '',
    cashout: '',
  });

  const fetchBuyin = async () => {
    const response = await api.get('/buy_ins/');
    setBuyin(response.data);
  };

  useEffect(() => {
    fetchBuyin();
  }, []);

  const handleChange = (event) => {
    const value = event.target.value;
    setFormData({
      ...formData,
      [event.target.name]: value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    await api.post('/buy_ins/', formData);
  };


}

export default App;
