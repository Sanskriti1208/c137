// App.js
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './screens/HomeScreen';
import StarListScreen from './screens/StarListScreen';
import StarDetailScreen from './screens/StarDetailScreen';

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="StarList" component={StarListScreen} />
        <Stack.Screen name="StarDetail" component={StarDetailScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
