import React from 'react';
import { StyleSheet, Text, View, ImageBackground, Dimensions, TouchableOpacity, KeyboardAvoidingView, Button, ActivityIndicator  } from 'react-native';
import { TextInput } from 'react-native-gesture-handler';
import Icon from 'react-native-vector-icons/Ionicons';

import background from '././src/background.jpg'

const { width: WIDTH } = Dimensions.get('window');

 class Scuarto extends React.Component {

   constructor(props){
       super(props);
       this.state ={ isLoading: true}

     }

     componentDidMount(){
       return fetch('https://mace2.github.io/json.json')
         .then((response) => response.json())
         .then((responseJson) => {

           this.setState({
             isLoading: false,
             dataSource: responseJson[0],
             local_q: responseJson[0].local_q2 + "",
             visitor_q: responseJson[0].visitor_q2 + ""
           }, function(){

           });

         })
         .catch((error) =>{
           console.error(error);
         });
     }



  render(){
    var {navigate} = this.props.navigation;
    if(this.state.isLoading){
      return(
        <View style={{flex: 1, padding: 20}}>
          <ActivityIndicator/>
        </View>
      )
    }

    return (

      <KeyboardAvoidingView behavior="padding" style={styles.container}>
      <ImageBackground source={background} style={styles.container}>

      <View style={styles.matchcontainer}>

      <Text style={styles.match1}>
        {this.state.dataSource.team_local}
      </Text>
      <View style={styles.inputContainer}>
        <Icon name={'ios-basketball'} size={28} color={'rgba(255, 255, 255, 0.7)'}
        style={styles.inputIcon}/>
        <TextInput
        style={styles.input}
        placeholder={this.state.local_q}
        placeholderTextColor={'rgba(255,255,255, 2)'}
        underlineColorAndroid='transparent'
        />
      </View>
      <Text style={styles.vs}>
        VS
      </Text>
      <Text style={styles.match2}>
        {this.state.dataSource.team_visitor}
      </Text>
      <View style={styles.inputContainer}>
        <Icon name={'ios-basketball'} size={28} color={'rgba(255, 255, 255, 0.7)'}
        style={styles.inputIcon}/>
        <TextInput
        style={styles.input}
        placeholder={this.state.visitor_q}
        placeholderTextColor={'rgba(255,255,255, 2)'}
        underlineColorAndroid='transparent'
        />
      </View>

      </View>

      <View style={styles.fullcontainer}>
      <TouchableOpacity style={styles.btnLogin} onPress={() => navigate('Third')}>
        <Text style={styles.text} > Reportar </Text>
      </TouchableOpacity>

      </View>

      </ImageBackground>
      </KeyboardAvoidingView>

    );
  }
}
export default Scuarto;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f8ff',
    justifyContent: 'center',
  },
  title:{
    color: 'rgba(255,255,255,10)',
    fontSize: 18,
    textAlign: 'center',
    marginTop: 1,
    marginBottom: 20,
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
  inputContainer: {
    marginTop: 1,
  },
  input: {
    width: WIDTH - 55,
    height: 45,
    borderRadius: 45,
    fontSize: 16,
    paddingLeft: 45,
    backgroundColor: 'rgba(0,0,0,.50)',
    color: 'rgba(255,255,255,0.9)',
    marginHorizontal: 25,
    },
    inputIcon: {
      position: 'absolute',
      top: 10 ,
      left: 37,
    },
  fullcontainer:{
      flexDirection: 'row',
      marginTop: 30,
      marginHorizontal: 5,
  },
  btnLogin :{
    width: WIDTH - 220,
    height: 45,
    borderRadius: 45,
    backgroundColor: 'rgba(220,20,60,50)',
    marginHorizontal: 109,
    marginTop: 1
  },
    text :{
    color: 'rgba(255,255,255,10)',
    fontSize: 23,
    textAlign: 'center',
    marginTop: 7,
    },
    matchcontainer:{
      marginTop: 50,
      marginBottom: 25,

    },
    match1:{
      color: 'rgba(255,255,255,10)',
      fontSize: 30,
      fontWeight: 'bold',
      textAlign: 'center',
      justifyContent: 'center',

    },
    match2:{
      color: 'rgba(255,255,255,10)',
      fontSize: 30,
      fontWeight: 'bold',
      textAlign: 'center',
      justifyContent: 'center',
      marginTop: 50,
    },
    vs:{
      marginTop: 50,
      color: 'rgba(0,0,0,10)',
      fontSize: 30,
      fontWeight: 'bold',
      textAlign: 'center',
      justifyContent: 'center',
    },
});
