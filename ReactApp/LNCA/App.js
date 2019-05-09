import React from 'react';
import { StyleSheet, Text, View, ImageBackground, Dimensions, TouchableOpacity, KeyboardAvoidingView, Button  } from 'react-native';
import { TextInput } from 'react-native-gesture-handler';
import {createStackNavigator, createAppContainer} from 'react-navigation';

import LoginScreen from './Login.js'
import CodeScreen from './Code.js'
import RegisterScreen from './Register.js'
import Pcuarto from './Pcuarto.js'
import Scuarto from './Scuarto.js'
import Tcuarto from './Tcuarto.js'
import Ccuarto from './Ccuarto.js'
import API from './Apirequest.js'


const Navigation = createStackNavigator({
  First: {screen: LoginScreen,
  navigationOptions: {
    header: null
    }
  },
  Second: {screen: CodeScreen,
  navigationOptions : {
    title: 'Codigo',
    headerTransparent: true,
    headerTintColor: '#f2f2f2',
    headerTitleStyle: {
      fontWeight: 'bold',
    },
  },
  },
  Third: {screen: RegisterScreen,
    navigationOptions : {
      headerTransparent: true,
      headerTintColor: '#f2f2f2',
      headerTitleStyle: {
        fontWeight: 'bold',
      },
    },
  },
  Fourth: {screen: Pcuarto,
    navigationOptions : {
      title: '1er Cuarto',
      headerTransparent: true,
      headerTintColor: '#f2f2f2',
      headerTitleStyle: {
        fontWeight: 'bold',
      },
    },
  },
  Fifth: {screen: Scuarto,
    navigationOptions : {
      title: '2do Cuarto',
      headerTransparent: true,
      headerTintColor: '#f2f2f2',
      headerTitleStyle: {
        fontWeight: 'bold',
      },
    },
  },
  Sixth: {screen: Tcuarto,
    navigationOptions : {
      title: '3er Cuarto',
      headerTransparent: true,
      headerTintColor: '#f2f2f2',
      headerTitleStyle: {
        fontWeight: 'bold',
      },
    },
  },
  Seventh: {screen: Ccuarto,
    navigationOptions : {
      title: '4to Cuarto',
      headerTransparent: true,
      headerTintColor: '#f2f2f2',
      headerTitleStyle: {
        fontWeight: 'bold',
      },
    },
  },
  Eight: {screen: API,
  navigationOptions : {
    title: 'Fetch Api',
    headerTransparent: true,
    headerTintColor: '#f2f2f2',
    headerTitleStyle: {
      fontWeight: 'bold',
      },
    },
  },
});

const App = createAppContainer(Navigation);
export default App;
