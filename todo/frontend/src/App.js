import './App.css';
import MyRoutes from './components/Routes';
// import { BrowserRouter } from 'react-router-dom';
import { HashRouter } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <HashRouter basename="/">
        {/* <BrowserRouter> */}
        <MyRoutes />
        {/* </BrowserRouter> */}
      </HashRouter>

    </div>
  );
}

export default App;
