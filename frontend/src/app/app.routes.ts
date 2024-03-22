import { Routes } from '@angular/router';
import { WorkspaceComponent } from './workspace/workspace.component';
import { CreateHabitComponent } from './create-habit/create-habit.component';

export const routes: Routes = [
  {
    path: 'workspaces/:id',
    component: WorkspaceComponent,
    title: 'Workspace'
  },
  {
    path: 'habits/create',
    component: CreateHabitComponent,
    title: 'Créer une habitude'
  }
];
