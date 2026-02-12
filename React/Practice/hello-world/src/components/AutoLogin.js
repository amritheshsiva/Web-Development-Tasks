import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { setUser } from "../store/authSlice";

function AutoLogin({ children }) {

  const dispatch = useDispatch();

  useEffect(() => {

    const token = localStorage.getItem("token");

    if (token) {
      dispatch(setUser({ token: token }));
    }

  }, []);

  return children;
}

export default AutoLogin;
