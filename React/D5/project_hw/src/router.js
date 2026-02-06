import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import Home from './components/Home'
import About from "./components/About";
import Contact from './components/Contact';

const router = createBrowserRouter([
    { path: '', element: <App/> },
    { path:'home',element:<Home/>},
    { path: 'about', element: <About/> },
    {path: 'contact',element:<Contact/>}
]);

export default router;
