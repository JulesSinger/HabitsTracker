import { Injectable } from '@angular/core';
import { Workspace } from './workspace';
@Injectable({
  providedIn: 'root'
})
export class WorkspacesService {

  constructor() { }

  workspaces: Workspace[] = [
    {
      id:1,
      name: 'Travail',
    },
    {
      id:2,
      name: 'Maison'
    },
    {
      id:3,
      name: 'Loisirs'
    }
  ]

  getAllWorkspaces(): Workspace[] {
    return this.workspaces;
  }

  getWorkspaceByid(id: number): Workspace | undefined {
    return this.workspaces.find(workspace => workspace.id === id);
  }
}
