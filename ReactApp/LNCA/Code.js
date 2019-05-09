import React from 'react';
import { StyleSheet, Text, View, ImageBackground, Dimensions, TouchableOpacity, KeyboardAvoidingView, Button  } from 'react-native';
import { TextInput } from 'react-native-gesture-handler';
import Icon from 'react-native-vector-icons/Ionicons';

import background from '././src/background.jpg'

const { width: WIDTH } = Dimensions.get('window');
export default class Code extends React.Component {
  

  render(){
    var {navigate} = this.props.navigation;
    return (

      <KeyboardAvoidingView behavior="padding" style={styles.container}>
      <ImageBackground source={background} style={styles.container}>

      <View style={styles.inputContainer}>
        <Icon name={'ios-basketball'} size={28} color={'rgba(255, 255, 255, 0.7)'}
        style={styles.inputIcon}/>
        <TextInput
        style={styles.input}
        placeholder={'Codigo de Partido'}
        placeholderTextColor={'rgba(255,255,255, 2)'}
        onChangeText={TextInputValue => this.setState({TextInputValue})}
        underlineColorAndroid='transparent'
        />
      </View>


      <TouchableOpacity style={styles.btnLogin} onPress={() =>{
      navigate("Third");
      }}>

      <Text style={styles.text} > Ir </Text>
      </TouchableOpacity>

      </ImageBackground>
      </KeyboardAvoidingView>


    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f8ff',
    justifyContent: 'center',
  },
  backgroundContainer:{
    flex: 1,
    width: null,
    height: null,
    justifyContent: 'center',
    alignItems: 'center',
  },
  Imagecontainer: {
    alignItems: 'center',
    marginBottom: 50,
  },
  logo: {
    width: 180,
    height: 180,
  },
  inputContainer: {
    marginTop: 10,
  },
  input: {
    width: WIDTH - 55,
    height: 45,
    borderRadius: 45,
    fontSize: 16,
    paddingLeft: 45,
    backgroundColor: 'rgba(0,0,0,.50)',
    color: 'rgba(255,255,255,0.7)',
    marginHorizontal: 25,
    },
    inputIcon: {
      position: 'absolute',
      top: 10 ,
      left: 37,
    },
    btnLogin :{
      width: WIDTH - 220,
      height: 45,
      borderRadius: 45,
      backgroundColor: 'rgba(220,20,60,50)',
      marginHorizontal: 109,
      marginTop: 30
    },
    text :{
    color: 'rgba(255,255,255,10)',
    fontSize: 16,
    textAlign: 'center',
    marginTop:10

    },
});
