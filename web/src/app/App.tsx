import type { Component } from 'solid-js';

import logo from '@assets/logo.svg';

import styles from '../App.module.scss';
import { Router } from '@solidjs/router';
import { routes } from './routes';
import { Layout } from '@widgets/Layout';


const App: Component = () => {
  return (
    <Router root={Layout}>
      {routes}
    </Router>
  );
};

export default App;
