import { RouteDefinition } from "@solidjs/router";
import { lazy } from "solid-js";

export const routes: RouteDefinition[] = [
  {
    path: '/login',
    component: lazy(() => import('@pages/Login'))
  },
  {
    path: '/budget/:budgetId',
    component: lazy(() => import('@pages/Budget'))
  }
]