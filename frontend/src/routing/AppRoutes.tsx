import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Routes } from '../config/variables';
import RegisterPage from '../common/pages/RegisterPage';
import MainPage from '../common/pages/MainPage';

const AppRoutes = () => {
  return (
    <Router>
      <Switch>
        <Route path={Routes.main} exact component={MainPage} />
        <Route path={Routes.register} exact component={RegisterPage} />
      </Switch>
    </Router>
  );
};

export default AppRoutes;
