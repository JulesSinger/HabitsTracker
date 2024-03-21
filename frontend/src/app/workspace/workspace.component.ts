import { Component } from '@angular/core';
import { HabitComponent } from '../habit/habit.component';
import { CommonModule } from '@angular/common';
import { Habit } from '../habit';

@Component({
  selector: 'app-workspace',
  standalone: true,
  imports: [
    HabitComponent,
    CommonModule
  ],
  templateUrl: './workspace.component.html',
  styleUrl: './workspace.component.scss'
})
export class WorkspaceComponent {
  habits: Habit[] = [
    {
      id: 1,
      title: 'Repasser mon linge',
    },
    {
      id:2,
      title: 'Lire'
    },
    {
      id:3,
      title: 'Faire mon lit'
    }
  ]
}
