// import { useNavigate } from "react-router-dom";

let Utils = {
    // navigate: useNavigate(),
    
    is_authenticated: () => {
        return !!localStorage.getItem('token');
    },

    // go_home: () => {
    //     this.navigate("/users", { replace: true });
    // }
    
}

export default Utils;