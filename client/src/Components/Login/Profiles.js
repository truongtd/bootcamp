import React,{Component} from 'react'

class Profile extends Component {
    constructor(props) {
      super(props);
      this.state = {
        error: null,
        isLoaded: false,
        items: []
      };
    }
    render(){
        return(
            <div>
                Profile
            </div>
        )
    }
}
export default Profile
