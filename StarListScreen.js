// screens/StarListScreen.js
import React, { useState, useEffect } from 'react';
import { View, Text, FlatList } from 'react-native';
import axios from 'axios';

const StarListScreen = ({ navigation }) => {
  const [stars, setStars] = useState([]);

  useEffect(() => {
    axios.get('http://your-api-url/stars')
      .then(response => {
        setStars(response.data);
      })
      .catch(error => {
        console.error('Error fetching stars:', error);
      });
  }, []);

  const renderItem = ({ item }) => (
    <Text onPress={() => navigation.navigate('StarDetail', { star: item })}>{item.star_name}</Text>
  );

  return (
    <View>
      <FlatList
        data={stars}
        renderItem={renderItem}
        keyExtractor={item => item.star_name}
      />
    </View>
  );
};

export default StarListScreen;
