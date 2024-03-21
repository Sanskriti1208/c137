// screens/StarDetailScreen.js
import React from 'react';
import { View, Text } from 'react-native';

const StarDetailScreen = ({ route }) => {
  const { star } = route.params;

  return (
    <View>
      <Text>Star Name: {star.star_name}</Text>
      <Text>Mass: {star.mass}</Text>
      <Text>Radius: {star.radius}</Text>
      <Text>Distance: {star.distance}</Text>
      <Text>Gravity: {star.gravity}</Text>
    </View>
  );
};

export default StarDetailScreen;
