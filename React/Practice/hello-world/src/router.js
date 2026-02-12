import { createBrowserRouter } from "react-router-dom";
import Aboutus from "./components/Aboutus";
import App from "./App";
import Greetings from './components/Greetings';
import Crud from './components/Crud';
import ListPost from './components/blog/ListPost'
import CreatePost from './components/blog/CreatePost'
import ViewPost from './components/blog/ViewPost'
import EditPost from './components/blog/EditPost'
import Register from './components/auth/register'
import Login from "./components/auth/Login";


const router = createBrowserRouter([
    { path: '', element: <App/> },
    { path: 'aboutus', element: <Aboutus/> },
    { path: 'greeting/:name', element: <Greetings/>},
    {path:'crud',element:<Crud/>},
    { path: 'listpost', element: <ListPost/> },
    { path : 'blog/posts/create' , element : <CreatePost/> },
    { path: 'blog/posts/:postId', element: <ViewPost/>},,
    { path : '/blog/posts/:postId/edit', element: <EditPost/>},
    { path: 'register', element:<Register/>},
    { path: "login", element: <Login /> }

]);

export default router;