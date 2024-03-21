import { Component, Input } from '@angular/core';
import { Habit } from '../habit';

@Component({
  selector: 'app-habit',
  standalone: true,
  imports: [],
  templateUrl: './habit.component.html',
  styleUrl: './habit.component.scss'
})
export class HabitComponent {
  @Input() habit!: Habit;
}
