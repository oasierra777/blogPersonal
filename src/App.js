import store from "./store";
import { Provider } from "react-redux";
import { BrowserRouter as Router, Route, Routes, Link, useLocation } from "react-router-dom";
import { Helmet, HelmetProvider } from 'react-helmet-async';

import AnimatedRouters from 'Routes'



function App() {

  return (
    <HelmetProvider>
      <Helmet>
        <title>Sisof | Software Agency</title>
        <meta name="description" content="Agencia de software"/>
        <meta name="keywords" content="agencia de software" />
        <meta name="robots" content="all" />
        <link rel="canonical" href="https://www.sisoft.com/" />
        <meta name="author" content="Sisoft" />
        <meta name="publisher" content="Sisoft" />

      </Helmet>
      <Provider store={store}>
        <Router>
          <AnimatedRouters/>
        </Router>
      </Provider>
    </HelmetProvider>
  );
}

export default App;
