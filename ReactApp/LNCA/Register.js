import React from 'react';
import { StyleSheet, Text, View, ImageBackground, Dimensions, TouchableOpacity, KeyboardAvoidingView, Button, ActivityIndicator, FlatList  } from 'react-native';
import { TextInput } from 'react-native-gesture-handler';
import Icon from 'react-native-vector-icons/Ionicons';

import background from '././src/background.jpg'

const { width: WIDTH } = Dimensions.get('window');
 class Register extends React.Component {

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

      <ImageBackground source={background} style={styles.container}>

      <Text style={styles.match}>
      {this.state.dataSource.team_local} vs {this.state.dataSource.team_visitor}
      </Text>

      <Text style={styles.score}>
      {this.state.dataSource.local_points} - {this.state.dataSource.visitor_points}
      </Text>

      <View style={styles.fullcontainer}>
      <TouchableOpacity style={styles.btnLogin1st} onPress={() => navigate('Fourth')}>
        <Text style={styles.text} > 1er{"\n"} Cuarto </Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.btnLogin1st} onPress={() => navigate('Fifth')}>
        <Text style={styles.text} > 2do{"\n"} Cuarto </Text>
      </TouchableOpacity>
      </View>

      <View style={styles.fullcontainer2}>
      <TouchableOpacity style={styles.btnLogin2nd} onPress={() => navigate('Sixth')}>
        <Text style={styles.text2} > 3er{"\n"} Cuarto </Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.btnLogin2nd} onPress={() => navigate('Seventh')}>
        <Text style={styles.text2} > 4to{"\n"} Cuarto </Text>
      </TouchableOpacity>
      </View>

      <TouchableOpacity style={styles.btnFoto} onPress={() => navigate('Eight')}>
        <Text style={styles.textfoto} > Subir foto </Text>
      </TouchableOpacity>


      </ImageBackground>



    );
  }
}
export default Register;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f8ff',
  },
  loader:{
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#fff"
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
  fullcontainer:{
      flexDirection: 'row',
      marginTop: 30,
      marginHorizontal: 25,
  },
  fullcontainer2:{
    flexDirection: 'row',
    marginHorizontal: 25,
  },
    btnLogin1st :{
      justifyContent: 'center',
      alignItems:'center',
      width: WIDTH - 230,
      height: 170,
      backgroundColor: 'rgba(220,20,60,50)',
      marginHorizontal: 10,
      borderRadius: 10,
    },
    btnLogin2nd:{
      width: WIDTH - 230,
      height: 170,
      backgroundColor: 'rgba(220,20,60,50)',
      marginHorizontal: 10,
      marginTop: 20,
      borderRadius: 10,

    },
    btnFoto:{
      width: WIDTH - 150,
      height: 50,
      backgroundColor: 'rgba(0,0,0,0.9)',
      marginHorizontal: 75,
      marginTop: 40,
      borderRadius: 10,
    },
    text :{
    color: 'rgba(255,255,255,10)',
    fontSize: 28,
    textAlign: 'center',
    marginTop: 10,
    },
    text2 :{
    color: 'rgba(255,255,255,10)',
    fontSize: 28,
    textAlign: 'center',
    marginTop: 50,
    },
    textfoto:{
      color: 'rgba(255,255,255,10)',
      fontSize: 28,
      textAlign: 'center',
      marginTop: 5,
    },
    match:{
      textAlign: 'center',
      justifyContent: 'center',
      fontSize: 23,
      color: 'rgba(255,255,255,10)',
      marginTop: 70,
      marginBottom: 1,
      fontWeight: 'bold'
    },
    score:{
      textAlign: 'center',
      justifyContent: 'center',
      fontSize: 20,
      color: 'rgba(255,255,255,10)',
      marginTop:1,
      marginBottom:10

    }
});
