import { Component, inject } from '@angular/core';
import { HabitComponent } from '../habit/habit.component';
import { CommonModule } from '@angular/common';
import { Habit } from '../habit';
import { Workspace } from '../workspace';
import { HabitsService } from '../habits.service';
import { WorkspacesService } from '../workspaces.service';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-workspace',
  standalone: true,
  imports: [
    HabitComponent,
    CommonModule,
    RouterModule
  ],
  templateUrl: './workspace.component.html',
  styleUrl: './workspace.component.scss'
})

export class WorkspaceComponent {
  habits: Habit[] = []
  habitsService: HabitsService = inject(HabitsService)

  workspaces: Workspace[] = []
  workspacesService: WorkspacesService = inject(WorkspacesService)
  
  constructor() {
    this.habitsService.getAllHabits().then(habits => this.habits = habits)
    this.workspaces = this.workspacesService.getAllWorkspaces()
  }
}
