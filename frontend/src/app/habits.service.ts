import { Injectable } from '@angular/core';
import { Habit } from './habit';
@Injectable({
  providedIn: 'root'
})
export class HabitsService {

  constructor() { }

  url = 'http://localhost:3000/habits'

  async getAllHabits(): Promise<Habit[]> {
    const response = await fetch(this.url)
    return await response.json() ?? []
  }

  async getHabitByid(id: number): Promise<Habit | undefined>  {
    const response = await fetch(`${this.url}/${id}`)
    return await response.json()
  }

  createHabit(title: string)  {
    console.log('Application submitted with:', title);
  }
}
